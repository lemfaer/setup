class atemplate(object):
	name = "atemplate"
	style = "snakeCase" # can also be snakeCase
	getter = """
	/**
	 * Gets the %(description)s.
	 *
	 * @return %(type)s
	 */
	public function get_%(normalizedName)s() {
		return $this->%(name)s;
	}
	"""

	setter = """
	/**
	 * Sets the %(description)s.
	 *
	 * @param %(type)s $%(name)s the %(humanName)s
	 * @return self
	 */
	public function set_%(normalizedName)s(%(typeHint)s $%(name)s) {
		$this->%(name)s = $%(name)s;
		return $this;
	}
	"""