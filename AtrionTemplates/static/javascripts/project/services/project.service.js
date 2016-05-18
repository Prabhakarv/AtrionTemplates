

(function () {
    'use strict';
    angular.module('thinkster.projects.services')
    .factory('Project', function ($resource) {
        return $resource('/api/v1/projects/');
    })
    .factory('Employee', function ($resource) {
        return $resource('/api/v1/employees/');
    })
    .factory('Customer', function ($resource) {
        return $resource('/api/v1/customers/');
    })
})();


