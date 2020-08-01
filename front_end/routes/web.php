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

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');
Route::get('/pages/color', 'DashController@color');
Route::get('/pages/typography', 'DashController@typography');
Route::get("/pages/charts" ,'DashController@charts');
Route::get("/pages/widgets" ,'DashController@widgets');

//routh group,paths with the same priffix
Route::prefix('/pages/buttons')->group(function (){
    Route::get('/button','DashController@button');
    Route::get('/brand-groups','DashController@brand');
});
