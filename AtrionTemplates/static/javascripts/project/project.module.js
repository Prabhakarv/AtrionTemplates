(function () {
    'use strict';

   var app=angular
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

    app.filter('propsFilter', function () {
        return function(items, props) {
            var out = [];

            if (angular.isArray(items)) {
                items.forEach(function(item) {
                    var itemMatches = false;

                    var keys = Object.keys(props);
                    for (var i = 0; i < keys.length; i++) {
                        var prop = keys[i];
                        var text = props[prop].toLowerCase();
                        if (item[prop].toString().toLowerCase().indexOf(text) !== -1) {
                            itemMatches = true;
                            break;
                        }
                    }

                    if (itemMatches) {
                        out.push(item);
                    }
                });
            } else {
                // Let the output be the input untouched
                out = items;
            }

            return out;
        }
    });

    angular
      .module('thinkster.projects.services', []);
})();