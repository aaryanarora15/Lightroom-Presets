def create_xmp_preset(filename, settings):
    """
    Creates a Lightroom .xmp preset file from a dictionary of settings.
    Just change the values in the settings dict and run the script!
    """

    xmp_content = f"""<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
      xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
      crs:PresetType="Normal"
      crs:ProcessVersion="11.0"
      crs:WhiteBalance="Custom"
      crs:Temperature="{settings['Temperature']}"
      crs:Tint="{settings['Tint']}"
      crs:Exposure2012="{settings['Exposure']}"
      crs:Contrast2012="{settings['Contrast']}"
      crs:Highlights2012="{settings['Highlights']}"
      crs:Shadows2012="{settings['Shadows']}"
      crs:Whites2012="{settings['Whites']}"
      crs:Blacks2012="{settings['Blacks']}"
      crs:Clarity2012="{settings['Clarity']}"
      crs:Dehaze="{settings['Dehaze']}"
      crs:Texture="{settings['Texture']}"
      crs:Vibrance="{settings['Vibrance']}"
      crs:Saturation="{settings['Saturation']}"
      crs:HueAdjustmentOrange="{settings['HueOrange']}"
      crs:HueAdjustmentGreen="{settings['HueGreen']}"
      crs:HueAdjustmentAqua="{settings['HueAqua']}"
      crs:HueAdjustmentBlue="{settings['HueBlue']}"
      crs:SaturationAdjustmentOrange="{settings['SatOrange']}"
      crs:SaturationAdjustmentGreen="{settings['SatGreen']}"
      crs:SaturationAdjustmentAqua="{settings['SatAqua']}"
      crs:SaturationAdjustmentBlue="{settings['SatBlue']}"
      crs:LuminanceAdjustmentOrange="{settings['LumOrange']}"
      crs:SplitToningShadowHue="{settings['ShadowHue']}"
      crs:SplitToningShadowSaturation="{settings['ShadowSat']}"
      crs:SplitToningHighlightHue="{settings['HighlightHue']}"
      crs:SplitToningHighlightSaturation="{settings['HighlightSat']}"
      crs:VignetteAmount="{settings['Vignette']}"
      crs:GrainAmount="{settings['Grain']}"
      crs:Name="{settings['Name']}">
      <crs:ToneCurvePV2012>
        <rdf:Seq>
          <rdf:li>0, 0</rdf:li>
          <rdf:li>64, {settings['CurveShadow']}</rdf:li>
          <rdf:li>128, {settings['CurveMid']}</rdf:li>
          <rdf:li>192, {settings['CurveHighlight']}</rdf:li>
          <rdf:li>255, 245</rdf:li>
        </rdf:Seq>
      </crs:ToneCurvePV2012>
      <crs:ToneCurvePV2012Blue>
        <rdf:Seq>
          <rdf:li>0, 0</rdf:li>
          <rdf:li>64, {settings['BlueShadow']}</rdf:li>
          <rdf:li>255, 255</rdf:li>
        </rdf:Seq>
      </crs:ToneCurvePV2012Blue>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

    with open(filename, 'w') as f:
        f.write(xmp_content)

    print(f"✅ Preset '{settings['Name']}' saved as {filename}")


# -------------------------------------------------------
# YOUR PRESETS — just change values here to make your own!
# -------------------------------------------------------

presets = [

    {
        "Name": "OrangeTeal Cinematic",   # name shown in Lightroom
        # -- Light --
        "Exposure":    "-0.20",
        "Contrast":    "+45",
        "Highlights":  "-60",
        "Shadows":     "-40",
        "Whites":      "+10",
        "Blacks":      "-70",   # crushed blacks = cinematic look
        # -- Color --
        "Temperature": "6000",  # warmth (higher = warmer)
        "Tint":        "+10",
        "Vibrance":    "-20",
        "Saturation":  "-15",
        # -- Effects --
        "Clarity":     "+10",
        "Dehaze":      "+10",
        "Texture":     "+10",
        "Vignette":    "-25",
        "Grain":       "0",
        # -- HSL Mix --
        "HueOrange":   "+15",   "SatOrange":  "+30",   "LumOrange": "+10",
        "HueGreen":    "-30",   "SatGreen":   "-40",
        "HueAqua":     "-20",   "SatAqua":    "+25",
        "HueBlue":     "-15",   "SatBlue":    "+20",
        # -- Split Toning (shadows=teal, highlights=warm) --
        "ShadowHue":      "210",  "ShadowSat":    "10",
        "HighlightHue":   "35",   "HighlightSat": "8",
        # -- Tone Curve --
        "CurveShadow":    "45",
        "CurveMid":       "110",
        "CurveHighlight": "175",
        "BlueShadow":     "75",   # adds blue to shadows
    },

    {
        "Name": "Golden Hour Cinematic",
        "Exposure":    "-0.30",
        "Contrast":    "+50",
        "Highlights":  "-70",
        "Shadows":     "-30",
        "Whites":      "+15",
        "Blacks":      "-65",
        "Temperature": "7000",  # very warm
        "Tint":        "+12",
        "Vibrance":    "-10",
        "Saturation":  "-10",
        "Clarity":     "+15",
        "Dehaze":      "+15",
        "Texture":     "+12",
        "Vignette":    "-30",
        "Grain":       "0",
        "HueOrange":   "+20",   "SatOrange":  "+40",   "LumOrange": "+15",
        "HueGreen":    "-25",   "SatGreen":   "-35",
        "HueAqua":     "-15",   "SatAqua":    "+15",
        "HueBlue":     "-10",   "SatBlue":    "+10",
        "ShadowHue":      "220",  "ShadowSat":    "12",
        "HighlightHue":   "30",   "HighlightSat": "10",
        "CurveShadow":    "40",
        "CurveMid":       "108",
        "CurveHighlight": "180",
        "BlueShadow":     "78",
    },

    {
        "Name": "Moody Night",
        "Exposure":    "-0.50",
        "Contrast":    "+55",
        "Highlights":  "-50",
        "Shadows":     "-50",
        "Whites":      "-10",
        "Blacks":      "-80",
        "Temperature": "4500",  # cool/blue
        "Tint":        "+5",
        "Vibrance":    "-25",
        "Saturation":  "-20",
        "Clarity":     "+20",
        "Dehaze":      "+20",
        "Texture":     "+15",
        "Vignette":    "-40",
        "Grain":       "0",
        "HueOrange":   "+10",   "SatOrange":  "+20",   "LumOrange": "0",
        "HueGreen":    "-20",   "SatGreen":   "-45",
        "HueAqua":     "-25",   "SatAqua":    "+30",
        "HueBlue":     "-20",   "SatBlue":    "+35",
        "ShadowHue":      "230",  "ShadowSat":    "18",
        "HighlightHue":   "40",   "HighlightSat": "6",
        "CurveShadow":    "28",
        "CurveMid":       "100",
        "CurveHighlight": "185",
        "BlueShadow":     "100",
    },

    {
        "Name": "Silhouette Sunset",
        "Exposure":    "-0.70",
        "Contrast":    "+60",
        "Highlights":  "-80",
        "Shadows":     "-60",
        "Whites":      "+20",
        "Blacks":      "-90",   # maximum crushed blacks for silhouettes
        "Temperature": "6500",
        "Tint":        "+15",
        "Vibrance":    "-5",
        "Saturation":  "-5",
        "Clarity":     "+10",
        "Dehaze":      "+20",
        "Texture":     "+8",
        "Vignette":    "-35",
        "Grain":       "0",
        "HueOrange":   "+25",   "SatOrange":  "+50",   "LumOrange": "+20",
        "HueGreen":    "-15",   "SatGreen":   "-30",
        "HueAqua":     "-10",   "SatAqua":    "+10",
        "HueBlue":     "-5",    "SatBlue":    "+5",
        "ShadowHue":      "225",  "ShadowSat":    "15",
        "HighlightHue":   "25",   "HighlightSat": "15",
        "CurveShadow":    "20",
        "CurveMid":       "95",
        "CurveHighlight": "175",
        "BlueShadow":     "70",
    },

]

# -- Run it — creates all preset files --
for preset in presets:
    filename = preset['Name'].replace(' ', '_') + '.xmp'
    create_xmp_preset(filename, preset)

print("\n🎬 All presets created! Import the .xmp files into Lightroom.")
