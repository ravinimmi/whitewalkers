var mongoose = require('mongoose');

module.exports = mongoose.model('User',{
     facebook         : {
        id           : String,
        token        : String,
        name         : String,
        gender      : String,
        email        : String,
        profile_pic_url: String,
        birthday: String
    },
    google           : {
        id           : String,
        token        : String,
        name         : String,
        gender      : String,
        email        : String,
        profile_pic_url: String,
        birthday: String
    }
});