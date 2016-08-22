var sourceDir = './source/';
var buildDir = '../static/';

module.exports = {
  views: './views/*',
  src: {
    root:     sourceDir,
    assets:   sourceDir + 'assets/',
    icons:    sourceDir + 'assets/icons',
    images:   sourceDir + 'assets/images',
    sass:     sourceDir + 'assets/sass',
    js:       sourceDir + 'js/',
    vendorJs: sourceDir + 'js/vendor',
    jsEntries: [
              sourceDir + 'js/index.js'
    ],
  },
  dist: {
    root:     buildDir,
    assets:   buildDir + 'assets/',
    css:      buildDir + 'assets/css',
    js:       buildDir + 'js/'
  }
};
