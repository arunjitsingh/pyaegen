module.exports = function(grunt) {
  var banner =
      '/** <%= pkg.name %> - v<%= pkg.version %>\n' +
      ' * Copyright <%= grunt.template.today("yyyy") %> Arunjit Singh\n' +
      ' * All Rights Reserved\n' +
      ' * [github.com/arunjitsingh]\n' +
      ' */\n';

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    concat: {
      options: {
        separator: ';'
      },
      build: {
        src: ['js/main.js'],
        dest: 'js/app.bundle.js'
      }
    },

    ngmin: {
      build: {
        src: 'js/app.bundle.js',
        dest: 'js/app.annotated.js'
      }
    },

    uglify: {
      options: {
        banner: banner
      },
      build: {
        src: 'js/app.annotated.js',
        dest: 'js/app.min.js'
      }
    },

    karma: {
      options: {
        browsers: ['Chrome'],
        port: 9876,
        runnerPort: 5100
      },
      unit: {
        configFile: 'unittest.conf.js',
        autoWatch: false,
        singleRun: true,

        coverage: {
          reporters: 'coverage'
        }
      },
      live: {
        configFile: 'unittest.conf.js',
        background: true
      }
    },

    watch: {
      karma: {
        files: ['js/**/*.js', 'jstests/**/*.js'],
        tasks: ['karma:live:run']
      }
    },

    clean: ['js/app.*.js', 'coverage']
  });

  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-ngmin');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-karma');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['concat', 'ngmin', 'uglify']);
  grunt.registerTask('test', ['karma:unit']);
  grunt.registerTask('coverage', ['karma:unit:coverage']);
  grunt.registerTask('livetest', ['karma:live', 'watch']);
};
