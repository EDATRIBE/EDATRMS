import Identicon from 'identicon.js'
import md5 from 'blueimp-md5'

export function GenAvatar(seed) {
    return 'data:image/png;base64,' + new Identicon(md5(seed), 420).toString()

}
