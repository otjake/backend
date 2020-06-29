<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class myFirstcontroller extends Controller
{
public function somefunction()
{
    $variableFromController = 'Sending data from controller to our web.php and displaying it with normal php';
    return view('subdirectory.hello',compact('variableFromController'));
}
public function forAppblade()
{
//    $variableFromController = 'Sending data from controller to our web.php and displaying it with normal php';
    return view('app');
}
public function forAboutblade()
{

    return view('about');
}
public function forServiceblade()
{
    $services=[
        "Service form controller 1",
        "Service form controller 2",
        "Service form controller 3",
        "Service form controller 4"
    ];
    //the array is left empty to show how @forelse and @empty works
    $about_service=[
    ];
//    $variableFromController = 'Sending data from controller to our web.php and displaying it with normal php';
    return view('services',compact('services','about_service'));
}

}
