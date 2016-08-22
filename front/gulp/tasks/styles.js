var paths = require('../paths');
var envs = require('../environments');
var autoprefixer = require('gulp-autoprefixer');
var plumber = require('gulp-plumber');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var gulpIf = require('gulp-if');

var onError = require('../handle-error');

module.exports = function (gulp) {
  return function (callback) {
    var isDev = process.env.GULP_ENV === paths.DEV;

    gulp.src(paths.src.sass + '/**/*.scss')
      .pipe(plumber({
        errorHandler: onError
      }))
      .pipe(gulpIf(isDev, sourcemaps.init()))
      .pipe(sass({
        outputStyle: isDev ? 'expanded' : 'compressed'
      }))
      .pipe(autoprefixer({
        browsers: ['last 2 versions', 'IE >= 9', '> 1%']
      }))
      .pipe(gulpIf(isDev, sourcemaps.write('.')))
      .pipe(gulp.dest(paths.dist.css))
      .on('end', callback);
  };
};
