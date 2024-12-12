import typescriptEslint from '@typescript-eslint/eslint-plugin';
import prettier from 'eslint-plugin-prettier';
import tsParser from '@typescript-eslint/parser';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import js from '@eslint/js';
import { FlatCompat } from '@eslint/eslintrc';

const compat = new FlatCompat({
	baseDirectory: path.dirname(fileURLToPath(import.meta.url)),
	recommendedConfig: js.configs.recommended,
	allConfig: js.configs.all,
});

export default [
	...compat.extends(
		'eslint:recommended',
		'plugin:@typescript-eslint/eslint-recommended',
		'plugin:@typescript-eslint/recommended',
		'prettier',
	),
	{
		plugins: {
			'@typescript-eslint': typescriptEslint,
			prettier,
		},
		languageOptions: {
			parser: tsParser,
		},
		rules: {
			'no-console': 1,
			'prettier/prettier': 2,
		},
		languageOptions: {
			globals: {
				...globals.node,
			},
		},
	},
];
