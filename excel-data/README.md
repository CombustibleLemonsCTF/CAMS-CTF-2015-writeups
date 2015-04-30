# CAMS CTF 2015: Excel Data

### Problem

**Points**: 30

**Description**: 

> Ever wonder why your homework gets corrupted so easily?  
> excel_data.xlsx

**Hint**: 

None given.

### Solution

Opening up the spreadsheet using conventional office software yields nothing of particular interest. To solve this challenge, you needed to look beneath the surface level of the file.

Excel spreadsheets are essentially specialized ZIP files, which means that they can also be extracted using your archive manager of choice. From there, it's simply a matter of searching the internal files: 

```
[!] ls
[Content_Types].xml  docProps  _rels  xl
[!] grep -R {
xl/styles.xml:<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="x14ac" xmlns:x14ac="http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac"><fonts count="1" x14ac:knownFonts="1"><font><sz val="11"/><color theme="1"/><name val="Calibri"/><family val="2"/><scheme val="minor"/></font></fonts><fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills><borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs><cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment horizontal="center"/></xf></cellXfs><cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles><dxfs count="0"/><tableStyles count="0" defaultTableStyle="TableStyleMedium2" defaultPivotStyle="PivotStyleLight16"/><extLst><ext uri="{EB79DEF2-80B8-43e5-95BD-54CBDDF9020C}" xmlns:x14="http://schemas.microsoft.com/office/spreadsheetml/2009/9/main"><x14:slicerStyles defaultSlicerStyle="SlicerStyleLight1"/></ext></extLst></styleSheet>
xl/charts/flag.txt:{iT's_r1gh7_h3r3}
```

**Flag**: `{iT's_r1gh7_h3r3}`

### Other Resources

* None.
