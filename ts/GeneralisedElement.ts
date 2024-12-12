// Hopefully more generalised. I may need to find a way to pass a list of type parameters though, or access the types from things that are passed,
// however I am unsure if I need infer for that or how the examples are able to access these types.
type GeneralisedElement<T> = {
	defaultProperty: T;
};

type ExtendedElement<Settings extends { useEmoji: boolean; useDiscovered: boolean }> = {
	text: string;
	emoji?: Settings['useEmoji'] extends true ? string : null;
	discovered?: Settings['useDiscovered'] extends true ? boolean : null;
	recipes?: any;
	otherStuff?: any;
};
