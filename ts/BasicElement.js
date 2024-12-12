'use strict';
function toNealCase(item) {
	try {
		// Implementation that should hopefully be consistent with Neal's
		return item
			.split(' ')
			.map(function (x) {
				return x.toLowerCase()[0].toUpperCase() + x.toLowerCase().slice(1);
			})
			.join(' ');
	} catch (err) {
		if (err instanceof Error) {
			if (err instanceof TypeError) {
				// Return undefined cause double space throw (simulating real game I guess?)
				return undefined;
			} else {
				// Dunno what happened.
				throw 'Unknown Error Occurred in toNealCase with input '.concat(item, ', message: ').concat(err.message);
			}
		}
	}
}
