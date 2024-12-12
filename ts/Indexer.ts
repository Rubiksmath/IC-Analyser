class Indexer<T> {
	// Hmm.... I need some kind of intelligent way to get the parameters to be generalised with some implicit stuff like extends and keyof and conditional types....
	// But I haven't had the pattern recognition and experience so I don't know what goes where and how I'd do that and the patterns to look out for for how I'd do it to help my make my decisions aaaa...
	public itemCount: number | null = null;
	public readonly options: T;

	constructor(options: T) {
		this.itemCount = 0;
		this.options = options;
	}

	public getProperty(item: uhh, property: GeneralProperty extends Property) {
        return item.idfk???
    }

	public addRecipe(ing1: BasicElement, ing2: BasicElement, result: BasicElement): void {

		let ing1_n = this.elementHandler.normaliseToKey(ing1);
		let ing2_n = this.elementHandler.normaliseToKey(ing2);
		let result_n = this.elementHandler.normaliseToKey(result);
	}
	
	public addConvertedRecipe(ing1Id, ing2Id, resultId): void {
		
	}
}
