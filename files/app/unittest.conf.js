basePath = '';

files = [
  JASMINE,
  JASMINE_ADAPTER,
  'components/angular/angular.js',
  'components/angular-mocks/angular-mocks.js',
  'js/**/*.js',
  'jstests/**/*.js'
];

exclude = [
  'jstests/**/*e2e*'
];

preprocessors = {
  'js/**/*.js': 'coverage'
};

reporters = ['dots', 'coverage'];

browsers = ['Chrome'];

port = 9876;
runnerPort = 5100;

colors = true;

autoWatch = true;
singleRun = false;
