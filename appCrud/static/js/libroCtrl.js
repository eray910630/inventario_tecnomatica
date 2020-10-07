/**
 * Created by adrian on 09/12/2016.
 */
app
.controller("libroCtrl", function($scope , API,$window){

        $scope.lista = [];
       var list = function(){
            API.Libro.list().$promise.then(function(r){
                $scope.lista = r;

            },function(err){
                console.log("Err " + err);

            });

        };

         list();

        $scope.sel = function(obj) {
            $scope.libro = API.Libro.get({ id: obj.id });

              };

       $scope.save = function(){

            if($scope.Libro.id){
                API.Libro.update({id : $scope.libro.id},$scope.libro).$promise.then(function(r){
                console.log("r: " + r);
                 list();
                     $scope.libro='';
                     },function(err){
                            console.log("Err " + err);

                     });


            }else{
                API.Libro.save($scope.libro).$promise.then(function(r){
                console.log("r: " + r);
                 list();
                    $scope.libro='';
                     },function(err){
                            console.log("Err " + err);

                     });
                 }

        };

//Funcion para eliminar pasando el id del objeto que deseamos eliminar

       $scope.delete = function(obj){
                    if($window.confirm('Seguro desea eliminar a : ?  ' +obj.nombre ))
                    {
                            API.Libro.delete({id: obj.id}, $scope.libro).$promise.then(function (r) {
                                console.log("r: " + r);
                                list();
                            }, function (err) {
                                console.log("Err " + err);

                            });

                    }
             };

               function colores(){
                  /* lista_colores=['class="active"','class="success"','class="warning"','class="danger"'];
                   for(i = 0; i < lista_colores.length; i++){
                        console.log(lista_colores[i]);
                   }*/


             };
                //colores()
    });


