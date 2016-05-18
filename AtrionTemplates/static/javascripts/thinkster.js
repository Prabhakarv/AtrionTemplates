(function () {
  'use strict';
console.log(" Prabhakar: im in thinkster app")
  	angular.module('thinkster', [
          'thinkster.config',
          'thinkster.routes',
          'thinkster.authentication',
          'thinkster.layout',
          'thinkster.projects',
          'thinkster.customers',
          'ngTable',
          'ngResource',
          'ngMaterial',
          'ngMessages',          
          //'material.svgAssetsCache'
        ]);


    angular.module('thinkster.config', 
      []);

  	angular.module('thinkster.routes', [
      'ngRoute'
      ]);  	


	  	angular.module('thinkster').run(run);

	run.$inject = ['$http'];

/**
* @name run
* @desc Update xsrf $http headers to align with Django's defaults
*/
function run($http) {
	console.log("inside run")
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}



})();