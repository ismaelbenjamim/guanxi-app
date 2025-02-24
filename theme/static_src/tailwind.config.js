/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                'cf-primary': '#6C63FF',   // Roxo-azulado (ex. do "Undraw")
                'cf-secondary': '#3B44F6', // Azul puxando pro roxo
                'cf-accent': '#B3B9FF',    // Azul claro para contrastes/elementos de destaque
                'cf-neutral': '#F0F4FF',   // Fundo branco/azulado
                'cf-dark': '#1B1D2F',      // Fundo ou texto escuro para contraste
                'cf-dark-light': '#212436', // Dark mais claro para equilíbrio visual
                'cf-muted': '#8A8FBF',     // Azul acinzentado para textos e detalhes sutis
                'cf-highlight': '#D6D9FF', // Azul pastel para realce suave
                'cf-border': '#CBD2FF',    // Azul-claro para bordas e separadores
                'cf-hover': '#564CE4',     // Tom mais escuro do primário para efeitos hover
                'cf-vibrant': '#9835E1',   // Roxo vibrante para elementos de destaque
            },
            fontFamily: {
                'sans': ['Inter', 'sans-serif'],
                'mono': ['Fira Code', 'monospace'],
                'poppins': ['Poppins', 'sans-serif'],
            }
        },
    },
    plugins:
        [
            /**
             * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
             * for forms. If you don't like it or have own styling for forms,
             * comment the line below to disable '@tailwindcss/forms'.
             */
            require('@tailwindcss/forms'),
            require('@tailwindcss/typography'),
            require('@tailwindcss/aspect-ratio'),
        ],
}
