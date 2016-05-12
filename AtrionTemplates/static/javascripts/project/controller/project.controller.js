/**
* ProfileController
* @namespace thinkster.profiles.controllers
*/
(function () {
    'use strict';

    angular
      .module('thinkster.projects.controllers', ['ngTable', 'ngAlertify'])
        .controller('ProjectController', function ($scope, Project, $http, Employee, alertify, Customer) {
            //alertify.alert("Hello, world!");
            $scope.status = {
                name: 'Initial'
            };
           
            $scope.projecttitle = {
                text: '',
                email:'',
                word: /^\s*\w*\s*$/
            };

            $scope.selectedItem;
            $scope.selectedCustomer;
            $scope.selectedCustomerid;
            $scope.selectedEmployeeid;

            //get the selectde employee from the dropdown
            $scope.dropboxitemselected = function (item) {
                $scope.selectedItem = item.employee_firstname;
                $scope.selectedEmployeeid = item.id;
              //  alert($scope.selectedEmployeeid);
            }

            //get the selectde customer from the dropdown
            $scope.dropboxcustomerselected = function (cust) {
                $scope.selectedCustomer = cust.cust_firstname;
                $scope.selectedCustomerid = cust.id;
                //  alert($scope.selectedEmployeeid);
            }

            //get all the employees
            var employeeEntries = Employee.query(function () {                
                $scope.Employeedata = employeeEntries;              
            });

            //get all the customers
            var customerEntries = Customer.query(function () {
                console.log(customerEntries)
                $scope.Customerdata = customerEntries;
            });

            //Get all the Project data
            var Projectentries = Project.query(function () {              
                $scope.Projectdata = Projectentries;
            });           

          


            //Create a new Project
            // Create an instance
            $scope.submit = function () {
                var newProject = new Project();
                newProject.project_name = $scope.projecttitle.text;
                newProject.project_status = $scope.status;
                alertify.alert($scope.status);
                var date = moment($scope.myDate).format('YYYY-MM-DD');
                newProject.employee_id = $scope.selectedEmployeeid
                newProject.customer_id = $scope.selectedCustomerid
                newProject.project_startdate = date;
                newProject.email = $scope.projecttitle.email;
                newProject.$save(function () { console.log('Project details saved'); });
            }

            //Date control Handler
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