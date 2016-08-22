var paths = require('../paths');

module.exports = function (gulp) {
  return function () {
    return gulp
      .src(paths.src.vendorJs + '**/*.js')
      .pipe(gulp.dest(paths.dist.js));
  };
};
