select p.productId,
	trim(p.baseSKU) as baseSKU,
    cn.productVariationId,
    cn.controlNumber,
    trim(pv.SKU) as sku,
    cn.quantity,
    -- cnl.LocationName,
    case when (p.productId <> 329) and coalesce(p.brand,'') != '' then concat(p.brand,' - ',p.name) else p.name end as productName,
    p.UPC,
    b.brand,
    p.model,
    p.msrpPrice,
    pv.quantity,
    pv.price,
    pv.retailPrice,
    pv.weightLbs,
    pv.width,
    pv.height,
    pv.depth,
    concat(case when cl.label is not null then concat(' - ',cl.label,':',cl.value) else '' end,
    case when ft.label is not null then concat(' - ',ft.label,':',ft.value) else '' end,
    case when wt.label is not null then concat(' - ',wt.label,':',wt.value) else '' end,
    case when td.label is not null then concat(' - ',td.label,':',td.value) else '' end,
    case when nk.label is not null then concat(' - ',nk.label,':',nk.value) else '' end,
    case when sv.label is not null then concat(' - ',sv.label,':',sv.value) else '' end,
    case when sn.label is not null then concat(' - ',sn.label,':',sn.value) else '' end,
    case when su.label is not null then concat(' - ',su.label,':',su.value) else '' end,
    case when ins.label is not null then concat(' - ',ins.label,':',ins.value) else '' end,
    case when wn.label is not null then concat(' - ',wn.label,':',wn.value) else '' end,
    case when ls.label is not null then concat(' - ',ls.label,':',ls.value) else '' end,
    case when ns.label is not null then concat(' - ',ns.label,':',ns.value) else '' end,
    case when se.label is not null then concat(' - ',se.label,':',se.value) else '' end,
    case when ch.label is not null then concat(' - ',ch.label,':',ch.value) else '' end) as size_lbl,
    -- coalesce(ft.value,wt.value,td.value,nk.value,sv.value,sn.value,su.value,ins.value,wn.value,ls.value,ns.value,se.value,ch.value) as size,
cl.value as color
   --   ,pv.updatedBy
from ProductControlNumbers cn
inner join ProductVariation pv on pv.productVariationID = cn.productVariationID
inner join Product p on p.productId = pv.productId
inner join Brand b on b.brandId = p.brandId
left join zzControlNumberLoc cnl on cnl.controlNumber = cn.controlNumber
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 18) cl on cl.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 85) sv on sv.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 86) ins on ins.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 87) td on td.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 88) wt on wt.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 89) ft on ft.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 90) se on se.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 91) ls on ls.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 92) ns on ns.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 93) wn on wn.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 94) su on su.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 95) ch on ch.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 96) nk on nk.productVariationId = cn.productVariationId
left join (select pa.productVariationId
                 ,av.value
                 ,a.label
           from ProductAttribute pa
           inner join AttributeValue av on av.attributeValueId = pa.attributeValueId
           inner join Attribute a on a.attributeId = av.attributeId
           where a.attributeId = 97) sn on sn.productVariationId = cn.productVariationId
-- where 1=1
   and pv.sku = '15742'
  -- and cn.productVariationId = 14250
  -- and p.baseSKU in ('p-15398')
 -- and p.productId = 16185
order by size_lbl desc
limit 10;