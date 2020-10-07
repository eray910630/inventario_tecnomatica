/**
 * Created by adrian on 27/11/2016.
 */


app.config(['$stateProvider', '$interpolateProvider','$httpProvider',
    function($stateProvider, $interpolateProvider,$httpProvider) {
    /* for compatibility with django teplate engine */
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    /* csrf */
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
}])
.config( function($resourceProvider) {
    /* for compatibility with django teplate engine */
           $resourceProvider.defaults.stripTrailingSlashes = false;

})
.config(function($stateProvider,$urlRouterProvider){



$stateProvider
             .state('index', {
                url: '/index',
                templateUrl: '/static/views/index.html'
            })

            .state('index.categorias', {
                url: '^/categorias',
                views:{
                    'tabledata@':{
                        templateUrl: '/static/views/categorias.html'
                    }
                }

            })

            .state('index.main', {
                url: '^/main',
                 views:{
                    'main@':{
                         templateUrl: '/static/views/nueva.html'
                    }
                }

            })
            .state("Home",{
                 url:"/",
                 templateUrl:"Home"
             })
            .state("test1",{
                 url:"/test1",
                 templateUrl:"test1"
            })
             .state("categoria",{
                 url:"/categorias",
                 templateUrl:"categorias"
            })
        $urlRouterProvider.otherwise("/nof");
  });