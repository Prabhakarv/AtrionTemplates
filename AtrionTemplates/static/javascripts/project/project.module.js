(function () {
    'use strict';

    angular
      .module('thinkster.projects', [
        'thinkster.projects.controllers',
        'thinkster.projects.services',
        'ngResource',
        "trNgGrid",
        "ngSanitize",
        "ui.select"
      ]);

    angular
      .module('thinkster.projects.controllers', []);

    angular
      .module('thinkster.projects.services', []);
})();