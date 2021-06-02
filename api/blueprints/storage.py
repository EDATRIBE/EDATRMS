import os

from sanic import Blueprint
from sanic.exceptions import NotFound
import aiofiles

from ..utilities import random_string
from ..models import StorageRegion, FileSchema
from ..services import StorageService
from .common import response_json, ResponseCode, authenticated_user

storage = Blueprint('storage', url_prefix='/storage')


@storage.post('/file/upload')
@authenticated_user()
async def upload(request):
    data = FileSchema().load(request.form)
    for key in ["region", "bucket", "path"]:
        if data.get(key) is None:
            return response_json(code=ResponseCode.FAILURE, message='Missing key: ' + key)

    region = data["region"]
    bucket = data["bucket"]
    path = data["path"]

    uploaded_files = []
    for i in range(request.app.config['UPLOAD_FILE_MAX_NUMBER']):
        uploaded_file = request.files.get('file{}'.format(i + 1))
        if uploaded_file is None:
            continue

        meta = {
            'name': uploaded_file.name,
            'type': uploaded_file.type,
            'size': len(uploaded_file.body),
        }
        if meta['size'] > request.app.config['UPLOAD_FILE_MAX_SIZE']:
            return response_json(code=ResponseCode.FAILURE, message='The size of \"{}\" exceeds the limit'.format(meta['name']))

        _, ext = os.path.splitext(meta['name'])
        filename = '{}{}'.format(random_string(16), ext)

        uploaded_files.append((meta, filename, uploaded_file.body))

    saved_files = []
    storage_service = StorageService(
        request.app.config, request.app.db, request.app.cache)
    if region == StorageRegion.LOCAL.value:
        save_dir = os.path.join(
            request.app.config['DATA_PATH'], request.app.config['FILES_DIR'],
            bucket, path)
        os.makedirs(save_dir, 0o755, True)

        for (meta, filename, body) in uploaded_files:
            async with aiofiles.open(
                    os.path.join(save_dir, filename), 'wb') as f:
                await f.write(body)

            file = await storage_service.create_file(
                region=region,
                bucket=bucket,
                path=os.path.join(path, filename),
                file_meta=meta,
                created_by=request['session']['user']['id'],
                updated_by=request['session']['user']['id']
            )

            saved_files.append(file)
    else:
        return response_json(code=ResponseCode.FAILURE, message='This region is not available')

    return response_json(
        files=[FileSchema().dump(v) for v in saved_files])


@storage.get('/file/info/<id:int>')
async def file_info(request, id):
    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    file = await storage_service.info(id)
    if file is None:
        raise NotFound('')

    return response_json(file=FileSchema().dump(file))


#filepond
@storage.post('/file/filepond/upload')
@authenticated_user()
async def upload_filepond_file(request):
    user_id = request['session']['user']['id']

    region = request.form.get('region', StorageRegion.LOCAL.value)
    bucket = request.form.get('bucket', 'image')
    path = request.form.get('path', '')

    uploaded_files = []
    for i in range(1):
        uploaded_file = request.files.get('file{}'.format(i+1))
        if uploaded_file is None:
            continue

        meta = {
            'name': uploaded_file.name,
            'type': uploaded_file.type,
            'size': len(uploaded_file.body),
        }
        if meta['size'] > request.app.config['UPLOAD_FILE_MAX_SIZE']:
            return response_json(code=ResponseCode.FAILURE,
                                 message='The size of \"{}\" exceeds the limit'.format(meta['name']))

        _, ext = os.path.splitext(meta['name'])
        filename = '{}{}'.format(random_string(16), ext)

        uploaded_files.append((meta, filename, uploaded_file.body))

    saved_files = []
    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    if region == StorageRegion.LOCAL.value:
        save_dir = os.path.join(
            request.app.config['DATA_PATH'],
            request.app.config['UPLOAD_DIR'],
            bucket, path
        )
        os.makedirs(save_dir, 0o755, True)

        for (meta, filename, body) in uploaded_files:
            async with aiofiles.open(os.path.join(save_dir, filename), 'wb') as f:
                await f.write(body)

            file = await storage_service.create(
                user_id=user_id, region=region, bucket=bucket,
                path=os.path.join(path, filename), meta=meta
            )

            saved_files.append(file)
    else:
        return response_json(ResponseCode.FAIL, 'This region is not supported')

    if len(saved_files) == 0:
        return response.text("0")

    return response.text(saved_files[0].get("id"))

@storage.get('/file/filepond/info/<id:int>')
@authenticated()
async def download_filepond_file(request,id):
    user_id = request['session'].get('user', {}).get('id')

    if id is not None:
        id = int(id)

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    file = await storage_service.info(id)
    if file is None:
        return response_json(ResponseCode.FAIL, 'Not found')

    if user_id != file['user_id']:
        return response_json(ResponseCode.FAIL, 'Access deny')

    file_path = os.path.join(
        config['DATA_PATH'],
        config['UPLOAD_DIR'],
        file['bucket'],
        file['path']
    )


    return await response.file(
        file_path,
        filename=file.get("meta").get("name", ''),
    )
