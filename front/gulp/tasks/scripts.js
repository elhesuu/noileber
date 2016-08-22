var path = require('path');
var gulp = require('gulp');
var named = require('vinyl-named');
var gutil = require('gulp-util');

var paths = require('../paths');
var envs = require('../environments');
var handleError = require('../handle-error');

module.exports = function (gulp) {
  var isProduction = process.env.GULP_ENV === envs.prod;

  return function () {
    return gulp;
  };
};