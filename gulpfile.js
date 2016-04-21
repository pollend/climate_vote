var gulp = require('gulp');
var ts = require('gulp-typescript');
var htmlmin = require('gulp-htmlmin');
var shell = require('gulp-shell');
var  watch = require('gulp-watch');
var batch = require('gulp-batch');
var sass = require('gulp-sass');

//build typescript
gulp.task('typescript', function () {
    return gulp.src('resource/typescript/**/*.ts')
        .pipe(ts({
        "target": "ES5",
        "module": "system",
        "moduleResolution": "node",
        "sourceMap": true,
        "emitDecoratorMetadata": true,
        "experimentalDecorators": true,
        "removeComments": true,
        "noImplicitAny": false
        }))
        .pipe(gulp.dest('src/app/static/typescript'));
});

// move templates from resource to the output directory
gulp.task('templates', function() {
    return gulp.src('resource/templates/**/*.html')
        .pipe(gulp.dest('src/app/static/templates'))
});

//builds the sass for the project
gulp.task('sass', function () {
    return gulp.src('resource/sass/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('src/app/static/css'));
});

// copy library dependencies 
gulp.task('lib', function() {
    gulp.src('node_modules/angular2/**/*').pipe(gulp.dest('src/app/static/angular2'));
    gulp.src('node_modules/rxjs/**/*').pipe(gulp.dest('src/app/static/rxjs'));
    gulp.src('node_modules/systemjs/**/*').pipe(gulp.dest('src/app/static/systemjs'));
    gulp.src('node_modules/es6-promise/**/*').pipe(gulp.dest('src/app/static/es6-promise'));
    gulp.src('node_modules/es6-shim/**/*').pipe(gulp.dest('src/app/static/es6-shim'));
    gulp.src('node_modules/zone.js/**/*').pipe(gulp.dest('src/app/static/zone.js'));
    gulp.src('node_modules/jquery/dist/**/*').pipe(gulp.dest('src/app/static/jquery'));
});

// builds the static files
gulp.task('build',['lib','templates','typescript','sass']);

// builds the project and runs the application
gulp.task('run',['build'],shell.task(['python src/run.py']));
// runs application with shell
gulp.task('run-shell',['build'],shell.task(['python src/shell.py']));

// watches source directory for changes and updates the associated files
gulp.task('watch',function(){
    gulp.start('lib');
    gulp.start('run');
    
    watch('resource/typescript/**/*.ts', batch(function (events, done) {
        gulp.start('typescript', done);
    }));
    watch('resource/templates/**/*.html', batch(function (events, done) {
        gulp.start('templates', done);
    }));
    watch('resource/sass/**/*.scss', batch(function (events, done) {
        gulp.start('sass', done);
    }));
});



// gulp.task('run')