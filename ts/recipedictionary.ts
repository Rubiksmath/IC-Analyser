type GeneralKeyType = number | [number, number] | string | [string, string];

type GeneralRecipeDictionary<KeyType, ValueType> = {
	// Index of type KeyType leads to ValueType - should correspond to any form of id: recipe combo
	[recipeId: KeyType]: ValueType;
};
