///**
//* Profile
//* @namespace thinkster.profiles.services
//*/
//(function () {
//    'use strict';

//    angular
//      .module('thinkster.projects.services')
//      .factory('Project',  function () {

//          function getAllProjects($http) {

//              return $http.get("/api/v1/projects/")
//          }

        

//      });

    

//    //Project.$inject = ['$http'];

//    //function Project($http) {

//    //    function getAllProjects($http) {
//    //        return $http.get("/api/v1/projects/")
//    //    }

//        //function getAllProjects($http) {
//        //    $http.get("/api/v1/projects/")
//        //       .then(function (response) {
//        //           $scope.myData = response.data;
//        //           return (JSON.stringify($scope.myData))
//        //       });
//        //}
    
//})();

(function () {
    'use strict';
    angular.module('thinkster.projects.services')
    .factory('Project', function ($resource) {
        return $resource('/api/v1/projects/');
    })
    .factory('Employee', function ($resource) {
        return $resource('/api/v1/employees/');
    })   
})();


//angular.module('thinkster.projects.services')    
//    .factory('Project', function ($resource) {
//        return $resource('/api/v1/projects/');
//    });