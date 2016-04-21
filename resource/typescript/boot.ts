/// <reference path="./../../node_modules/angular2/typings/browser.d.ts" />
/// <reference path="./../../typings/main.d.ts" />

// typings is a library to use non typescript libraries in typescript
// https://www.npmjs.com/package/typings

import {bootstrap}    from 'angular2/platform/browser';
import {AppComponent} from './app.component';


import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';
import {HTTP_PROVIDERS}    from 'angular2/http';


bootstrap(AppComponent,[
ROUTER_PROVIDERS,
	HTTP_PROVIDERS
]);
