var runSequence = require('run-sequence');
var browserSync = require('browser-sync');
var paths = require('../paths');

module.exports = function (gulp) {
  return function () {
    gulp.task('watch', function () {
      gulp.watch(paths.views, browserSync.reload);
      gulp.watch(paths.src.js + '/**/*.js', function () {
        return runSequence(['scripts'], browserSync.reload);
      });
      gulp.watch(paths.src.sass + '/**/*.scss', ['styles']);
      gulp.watch(paths.src.images + '/**/*', ['images']);
    });
  };
};