from numpy import sqrt

def hex_to_rgb(hex_string: str) -> tuple[int, int, int]:
    hex_string = hex_string.lstrip("#")
    return tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4))


def lightness_coef(hex_color: str) -> float:
    """
    Luma handles lighter colors better, while weighted euclidean
    norm handles darker colors better. Start with weighted euclidean
    norm, and if the color is medium to light, switch to luma
    """
    coef = weighted_euclidean_norm_rgb(hex_to_rgb(hex_color))
    if coef > 0.4:
        return luma_rgb(hex_to_rgb(hex_color))
    return coef


def color_is_light(hex_color: str) -> bool:
    min_to_be_considered_light = 0.525
    coef = lightness_coef(hex_color)
    if coef > min_to_be_considered_light:
        return True
    return False


def get_alt_shade(color: str, shade_coef: float | None = 0.4) -> str:
    try:
        from bokeh.colors import RGB
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "To use auto-shading, `bokeh` must be installed. Please 'pip install bokeh'"
        )
    
    downscale_lightness_strength = 5
    strengthen_weight_exponential = 2  # power

    is_light = color_is_light(color)
    lightness = lightness_coef(color)
    lightness_strength = abs(lightness - 0.5)
    if is_light is False:
        strengthen_weight_exponential += ((lightness_strength + 1) ** 3) - 1
        # downscale_lightness_strength -= 1
    lightness_strength_scaled = lightness_strength / downscale_lightness_strength
    weight_exp = ((lightness_strength_scaled + 1) ** strengthen_weight_exponential) - 1

    weight = weight_exp
    # print(round(weight * 10, 3), "-", strengthen_weight_exponential, "-", round(lightness_strength * 10, 3), "-", round(lightness * 10, 3))

    rgb = RGB(*hex_to_rgb(color))

    if is_light:
        res = rgb.darken(shade_coef + weight)
    else:
        res = rgb.lighten(shade_coef + weight)
    
    return res.to_hex().lstrip("#")


def luma_rgb(rgb: list | tuple) -> float:
    """
    Luma of rgb vector / 255
    """
    r, g, b = rgb
    return (
        (
            (0.212 * r)
            + (0.701 * g)
            + (0.087 * b)
        )
        / 255
    )


def weighted_euclidean_norm_rgb(rgb: list | tuple) -> float:
    """
    Dear programmer: I have no idea how this works, but it determines
    how 'light' a color is.

    Returns: float between 0 and 1
    """
    r, g, b = rgb
    denom = 255 * sqrt(0.299 + 0.587 + 0.114)
    return sqrt(0.299 * r**2 + 0.587 * g**2 + 0.114 * b**2) / denom




