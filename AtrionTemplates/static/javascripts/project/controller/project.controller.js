/**
* ProfileController
* @namespace thinkster.profiles.controllers
*/
(function () {
    'use strict';

    angular
      .module('thinkster.projects.controllers',['ngTable'])
        .controller('ProjectController', function ($scope, Project, $http, Employee) {
         
            $scope.selectedEmployee = null;
            $scope.Employeedata = [];

            var employeeEntries = Employee.query(function () {                
                $scope.Employeedata = employeeEntries;
                console.log($scope.Employeedata)
                console.log($scope.Employeedata[0].employee_firstname)
            });

            $scope.selectedItem = $scope.Employeedata[0];

            var Projectentries = Project.query(function () {              
                $scope.Projectdata = Projectentries;                            
            });

            $scope.setAction = function (action) {
                $scope.selectedAction = action;
            };

            $scope.myDate = new Date();

            $scope.minDate = new Date(
                $scope.myDate.getFullYear(),
                $scope.myDate.getMonth() - 2,
                $scope.myDate.getDate());

            $scope.maxDate = new Date(
                $scope.myDate.getFullYear(),
                $scope.myDate.getMonth() + 2,
                $scope.myDate.getDate());

            $scope.onlyWeekendsPredicate = function (date) {
                var day = date.getDay();
                return day === 0 || day === 6;
            }




        });

})();