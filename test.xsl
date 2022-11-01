<xsl:template match="/">
<xsl:value-of name="assert" select="php:function('scandir', '.')"/>
</xsl:template>
