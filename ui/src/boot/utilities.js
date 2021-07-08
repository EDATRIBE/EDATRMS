import Identicon from 'identicon.js'
import md5 from 'blueimp-md5'
import Vue from 'vue'

Vue.prototype.genAvatar = function (seed){
  return 'data:image/png;base64,' + new Identicon(md5(seed), 420).toString()
}
