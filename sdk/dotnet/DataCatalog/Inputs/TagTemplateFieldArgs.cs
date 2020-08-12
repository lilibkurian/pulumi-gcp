// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.DataCatalog.Inputs
{

    public sealed class TagTemplateFieldArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The display name for this template.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// The identifier for this object. Format specified above.
        /// </summary>
        [Input("fieldId", required: true)]
        public Input<string> FieldId { get; set; } = null!;

        /// <summary>
        /// Whether this is a required field. Defaults to false.
        /// </summary>
        [Input("isRequired")]
        public Input<bool>? IsRequired { get; set; }

        /// <summary>
        /// -
        /// The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The order of this field with respect to other fields in this tag template.
        /// A higher value indicates a more important field. The value can be negative.
        /// Multiple fields can have the same order, and field orders within a tag do not have to be sequential.
        /// </summary>
        [Input("order")]
        public Input<int>? Order { get; set; }

        /// <summary>
        /// The type of value this tag field can contain.
        /// Structure is documented below.
        /// </summary>
        [Input("type", required: true)]
        public Input<Inputs.TagTemplateFieldTypeArgs> Type { get; set; } = null!;

        public TagTemplateFieldArgs()
        {
        }
    }
}
