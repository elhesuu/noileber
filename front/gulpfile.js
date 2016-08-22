var gulp = require('gulp');
var envs = require('./gulp/environments');
var paths = require('./gulp/paths');
var runSequence = require('run-sequence');

var subtasks = [
  'styles',
  'scripts',
  'images',
  'watch',
  'copy',
  'clean',
];

subtasks.forEach(function(task) {
  var module = require('./gulp/tasks/' + task);
  gulp.task(task, module(gulp));
});

gulp.task('build', function (callback) {
  process.env.GULP_ENV = envs.prod;
  return runSequence('clean',
    ['scripts', 'styles', 'images', 'copy'],
    callback
   );
});

gulp.task('default', function (callback) {
  process.env.GULP_ENV = envs.dev;
  return runSequence(
    ['build', 'watch'],
    callback
  );
});