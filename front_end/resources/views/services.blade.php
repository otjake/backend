@extends('app')

{{--title for this page is set--}}
@section('title','Services')

{{--content for this page is set--}}
@section('content_area')
    <h1>Welcome to laravel service page</h1>
    <p>Welcome to laravel additional text for service page</p>
    <ul>
        <li>Service 1</li>
        <li>Service 2</li>
        <li>Service 3</li>
    </ul>
    <h1>grabbing services from our controller</h1>

    @foreach($services as $service)
        <li>{{ $service }}</li>
    @endforeach

    <h1>grabbing about_service from our controller with an "atEmpty" which is a else if the about_service array is empty do something else</h1>

    @forelse($about_service as $abservice)
        <li>{{ $abservice }}</li>
    @empty
        {{--        if $about_service is empty--}}
        <li>{{ "Our services have no abouts for now" }}</li>

    @endforelse
@endsection

