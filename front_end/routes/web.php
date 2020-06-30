<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
//note no file path name is empty here meaning root of our files
Route::get('/', function () {
    //return view('welcome') returns welcome page for laravel the html page can be found under resourses/views
    return view('welcome');
});
//first route uri serves as path to be typed in browser, uri can be  /hello/hello or anything just like file directories are specified
Route::get('/hello', function () {
    //content of path
    return view('hello');
});

//same file from a sub directory
//Route::get('/hello', function () {
//    $variableFromRoute = "Sending data from route and displaying it with blade syntax {{ $ arrayKey  }}";
//    $variableFromController = "Sending data from controller and displaying it with normal php";
   //content of path
////    return view('subdirectory.hello',['key'=>$variableFromRoute,
//       ]);


////    or if both key and array data name are the same we can use compact function
//     return view('subdirectory.hello',compact('variableFromRoute'));

//});

//    we can also display data from our controller,all our callback functions are moved to the controller under a public function/method with name index
Route::get('/hello','myFirstcontroller@somefunction');
Route::get('/app','myFirstcontroller@forAppblade');
Route::get('/about','myFirstcontroller@forAboutblade');
Route::get('/service','myFirstcontroller@forServiceblade');
