/**
 * @fileoverview ...
 *
 * @author arunjitsingh
 */
'use strict';

var main = angular.module('main', []);

main.config([
    '$locationProvider', '$routeProvider',
    function($locationProvider, $routeProvider) {
      $locationProvider.html5Mode(true);
      $routeProvider.
          when('/inline', {'templateUrl': '/inline/home.html'}).
          when('/', {'templateUrl': '/views/home.html'}).
          otherwise({'redirectTo': '/'});
    }
]);
