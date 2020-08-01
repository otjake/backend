<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class DashController extends Controller
{
    public function color(){
        return view("/pages/color");
    }

    public function typography(){
        return view("pages/typography");
    }
    public function charts(){
        return view("pages/charts");
    }

    public function widgets(){
        return view("pages/widgets");
    }

    //grouped routes
    public function button(){
        return view("pages/buttons/button");
    }
    public function brand(){
        return view("pages/buttons/brand-groups");
    }
}
