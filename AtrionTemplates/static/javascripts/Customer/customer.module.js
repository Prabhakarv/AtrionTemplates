(function () {
    'use strict';

    angular
      .module('thinkster.customers', [
        'thinkster.customers.controllers',
        'thinkster.customers.services',
        'ngResource',
        "trNgGrid"
      ]);

    angular
      .module('thinkster.customers.controllers', []);

    angular
      .module('thinkster.customers.services', []);
})();