// Basic element type, matches the game I guess... Required text field, and emoji, discovered, and recipes are optional.
// The recipes are a set of two strings, although I may need to find a better way. The general element may be able to handle this.
type BasicElement = {
	text: string;
	emoji?: string;
	discovered?: boolean;
	hidden?: boolean;
	recipes?: Set<[string, string]>;
};
