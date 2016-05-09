(function () {
  'use strict';
 console.log(" Prabhakar: im in angular route")
  angular
    .module('thinkster.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
   console.log(" Prabhakar: Registering the route template")
    $routeProvider.when('/register', {
      controller: 'RegisterController', 
      controllerAs: 'vm',
      templateUrl: '/static/templates/authentication/register.html'
    }).when('/login',{
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/authentication/login.html'
    }).when('/project', {
        controller: 'ProjectController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/project/Project.html'
    }).otherwise('/');
  }
})();


