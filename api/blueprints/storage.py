import os

import aiofiles
from sanic import Blueprint, response
from sanic.exceptions import NotFound

from ..models import FileSchema, StorageBucket, StorageRegion
from ..services import StorageService
from ..utilities import random_string
from .common import (ResponseCode, authenticated_user, not_null_validation,
                     response_json)

storage = Blueprint('storage', url_prefix='/storage')


@storage.post('/file/upload')
@authenticated_user()
async def upload(request):
    data = FileSchema().load(request.form)
    region = data.get("region",StorageRegion.LOCAL.value)
    bucket = data.get("bucket",StorageBucket.LIMBO.value)
    path = data.get("path",'')

    uploaded_files = []
    for i in range(request.app.config['UPLOAD_FILE_MAX_NUMBER']):
        uploaded_file = request.files.get('file{}'.format(i + 1))
        if uploaded_file is None:
            continue

        file_meta = {
            'name': uploaded_file.name,
            'type': uploaded_file.type,
            'size': len(uploaded_file.body),
        }
        if file_meta['size'] > request.app.config['UPLOAD_FILE_MAX_SIZE']:
            return response_json(
                code=ResponseCode.FAILURE,
                message='The size of \"{}\" exceeds the limit'.format(file_meta['name'])
            )

        _, ext = os.path.splitext(file_meta['name'])
        file_name = '{}{}'.format(random_string(16), ext)

        uploaded_files.append((file_meta, file_name, uploaded_file.body))

    saved_files = []
    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    if region == StorageRegion.LOCAL.value:
        save_dir = os.path.join(
            request.app.config['DATA_PATH'], request.app.config['LOCAL_FILES_DIR'],
            bucket, path)
        os.makedirs(save_dir, 0o755, True)

        for (file_meta, file_name, body) in uploaded_files:
            async with aiofiles.open(os.path.join(save_dir, file_name), 'wb') as f:
                await f.write(body)

            file = await storage_service.create_file(
                region=region,
                bucket=bucket,
                path=os.path.join(path, file_name),
                file_meta=file_meta,
                created_by=request['session']['user']['id'],
                updated_by=request['session']['user']['id']
            )

            saved_files.append(file)
    else:
        return response_json(code=ResponseCode.FAILURE, message='This region is not available')

    return response_json(
        files=[FileSchema().dump(v) for v in saved_files])


@storage.get('/file/info/<id:int>')
async def info(request, id):
    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    file = await storage_service.info(id)
    if file is None:
        raise NotFound('')

    return response_json(file=FileSchema().dump(file))


@storage.post('/file/filepond/upload')
@authenticated_user()
async def filepond_upload(request):
    region = StorageRegion.LOCAL.value
    bucket = StorageBucket.LIMBO.value
    path = ''

    uploaded_file = request.files.get('file_pond_file')
    if uploaded_file is None:
        return response_json(code=ResponseCode.DIRTY, message='Missing field: file_pond_file')

    file_meta = {
        'name': uploaded_file.name,
        'type': uploaded_file.type,
        'size': len(uploaded_file.body),
    }
    if file_meta['size'] > request.app.config['UPLOAD_FILE_MAX_SIZE']:
        return response_json(
            code=ResponseCode.FAILURE,
            message='The size of \"{}\" exceeds the limit'.format(file_meta['name'])
        )

    _, ext = os.path.splitext(file_meta['name'])
    file_name = '{}{}'.format(random_string(16), ext)

    save_dir = os.path.join(
        request.app.config['DATA_PATH'], request.app.config['LOCAL_FILES_DIR'],
        bucket, path
    )
    os.makedirs(save_dir, 0o755, True)
    async with aiofiles.open(os.path.join(save_dir, file_name), 'wb') as f:
        await f.write(uploaded_file.body)

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    file = await storage_service.create_file(
        region=region,
        bucket=bucket,
        path=os.path.join(path, file_name),
        file_meta=file_meta,
        created_by=request['session']['user']['id'],
        updated_by=request['session']['user']['id']
    )

    return response.text(file["id"])


@storage.get('/file/filepond/load/<id:int>')
async def filepond_load(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message='Missing file id')

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    file = await storage_service.info(id)
    if file is None:
        return response_json(code=ResponseCode.DIRTY, message='Not found')

    file_posi = os.path.join(
        request.app.config['DATA_PATH'],
        request.app.config['LOCAL_FILES_DIR'],
        file['bucket'],
        file['path']
    )

    return await response.file(file_posi, filename=file.get("file_meta",{}).get("name", ''))
