/**
 * Created by adrian on 27/11/2016.
 */

app.factory("API",function($resource) {

    var url = "http://127.0.0.1:8000/api/";

    return{
            Categoria: $resource(url + 'categorias/:id/', {'id': '@id'}, {

            "update": {method: 'PUT'},
            "list": {method: 'GET', isArray:true},

        }),
            Libro: $resource(url + 'libros/:id/', {'id': '@id'}, {

            "update": {method: 'PUT'},
            "list": {method: 'GET', isArray:true},

        }),
    };
});