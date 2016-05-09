/**
* ProfileController
* @namespace thinkster.profiles.controllers
*/
(function () {
    'use strict';

    angular
      .module(

                'thinkster.customers.controllers', ['ngTable'])
                .controller(
                                'CustomerController', function ($scope, Project, $http, Customer) {
                                    var customerEntries = Customer.query(function () {
                                        $scope.data = customerEntries;
                                        alert($scope.data)
                                    });
                                })
})();