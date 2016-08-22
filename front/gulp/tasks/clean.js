var clean = require('gulp-clean');

var paths = require('../paths');

module.exports = function (gulp) {
  return function () {
    return gulp.src([ paths.dist.root + '*' ], { read: false })
      .pipe(clean({ force: true }));
  };
};