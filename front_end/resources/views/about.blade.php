{{--//with @extend the about page can hold everything in the app page--}}
@extends('app')

{{--assigning a value to the @yield('title') in the app page--}}
@section('title','About us')

@section('content_area')
    <h1>Welcome to laravel about page</h1>
    <p>Welcome to laravel additional text for about page</p>


@endsection
