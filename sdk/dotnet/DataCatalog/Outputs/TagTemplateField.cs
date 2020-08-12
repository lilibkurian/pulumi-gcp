// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.DataCatalog.Outputs
{

    [OutputType]
    public sealed class TagTemplateField
    {
        /// <summary>
        /// The display name for this template.
        /// </summary>
        public readonly string? DisplayName;
        /// <summary>
        /// The identifier for this object. Format specified above.
        /// </summary>
        public readonly string FieldId;
        /// <summary>
        /// Whether this is a required field. Defaults to false.
        /// </summary>
        public readonly bool? IsRequired;
        /// <summary>
        /// -
        /// The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The order of this field with respect to other fields in this tag template.
        /// A higher value indicates a more important field. The value can be negative.
        /// Multiple fields can have the same order, and field orders within a tag do not have to be sequential.
        /// </summary>
        public readonly int? Order;
        /// <summary>
        /// The type of value this tag field can contain.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.TagTemplateFieldType Type;

        [OutputConstructor]
        private TagTemplateField(
            string? displayName,

            string fieldId,

            bool? isRequired,

            string? name,

            int? order,

            Outputs.TagTemplateFieldType type)
        {
            DisplayName = displayName;
            FieldId = fieldId;
            IsRequired = isRequired;
            Name = name;
            Order = order;
            Type = type;
        }
    }
}
