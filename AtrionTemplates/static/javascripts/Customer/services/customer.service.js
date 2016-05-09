angular.module('thinkster.customers.services')
    .factory('Customer', function ($resource) {
        return $resource('/api/v1/customers/');
    });