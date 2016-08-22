var imagemin = require('gulp-imagemin');
var gulpIf = require('gulp-if');

var paths = require('../paths');
var envs = require('../environments');

module.exports = function (gulp) {
  return function () {
    var isProduction = process.env.GULP_ENV === envs.prod;
    return gulp.src( paths.src.assets + 'images/**/*' )
      .pipe(gulpIf(isProduction, imagemin({
        optimizationLevel: 5,
        progressive: true,
        interlaced: true
      })))
      .pipe(gulp.dest( paths.dist.assets + 'images'));
  };
};