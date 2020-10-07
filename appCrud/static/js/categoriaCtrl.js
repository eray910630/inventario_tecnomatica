/**
 * Created by adrian on 27/11/2016.
 */
app
.controller("categoriaCtrl", function($scope , API, $window){


     /******Paginado*****/

      $scope.currentPage = 0;
      $scope.pageSize = 15;
      $scope.pages = [];


      /*****end paginado****/





       $scope.lista = [];

       var list = function(){

            API.Categoria.list().$promise.then(function(r){

                $scope.lista = r;
                $scope.configPages();


                //alert('pase por aqui');

            },function(err){
                console.log("Err " + err);

            });

        };

         list();

        $scope.sel = function(obj) {
            $scope.categoria = API.Categoria.get({ id: obj.id });

              };

       $scope.save = function(){

            if($scope.categoria.id){
                API.Categoria.update({id : $scope.categoria.id},$scope.categoria).$promise.then(function(r){
                console.log("r: " + r);
                 list();
                     $scope.categoria='';
                     },function(err){
                            console.log("Err " + err);

                     });


            }else{
                API.Categoria.save($scope.categoria).$promise.then(function(r){
                console.log("r: " + r);
                 list();
                    $scope.categoria='';
                     },function(err){
                            console.log("Err " + err);

                     });
                 }

        };

//Funcion para eliminar pasando el id del objeto que deseamos eliminar

       $scope.delete = function(obj){
                    if($window.confirm('Seguro desea eliminar a : ?  ' +obj.nombre ))
                    {
                            API.Categoria.delete({id: obj.id}, $scope.categoria).$promise.then(function (r) {
                                console.log("r: " + r);
                                list();
                            }, function (err) {
                                console.log("Err " + err);

                            });

                    }
             };


/*****************************************Begin Paginado*******************************************/


      $scope.configPages = function() {
        $scope.pages.length = 0;
        var ini = $scope.currentPage - 4;
        var fin = $scope.currentPage + 5;
        if (ini < 1) {
          ini = 1;
          if (Math.ceil($scope.lista.length / $scope.pageSize) > 10)
            fin = 10;
          else
            fin = Math.ceil($scope.lista.length / $scope.pageSize);
        } else {
          if (ini >= Math.ceil($scope.lista.length / $scope.pageSize) - 10) {
            ini = Math.ceil($scope.lista.length / $scope.pageSize) - 10;
            fin = Math.ceil($scope.lista.length / $scope.pageSize);
          }
        }
        if (ini < 1) ini = 1;
        for (var i = ini; i <= fin; i++) {
          $scope.pages.push({
            no: i
          });
        }

        if ($scope.currentPage >= $scope.pages.length)
          $scope.currentPage = $scope.pages.length - 1;
      };

      $scope.setPage = function(index) {
        $scope.currentPage = index - 1;
      };

    })

.filter('startFromGrid', function() {
  return function(input, start) {
    start = +start;
    return input.slice(start);
  }

        /******End paginado*****/
});

