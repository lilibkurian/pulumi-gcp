// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.DataCatalog.Inputs
{

    public sealed class EntryGcsFilesetSpecGetArgs : Pulumi.ResourceArgs
    {
        [Input("filePatterns", required: true)]
        private InputList<string>? _filePatterns;

        /// <summary>
        /// Patterns to identify a set of files in Google Cloud Storage.
        /// See [Cloud Storage documentation](https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames)
        /// for more information. Note that bucket wildcards are currently not supported. Examples of valid filePatterns:
        /// * gs://bucket_name/dir/*: matches all files within bucket_name/dir directory.
        /// * gs://bucket_name/dir/**: matches all files in bucket_name/dir spanning all subdirectories.
        /// * gs://bucket_name/file*: matches files prefixed by file in bucket_name
        /// * gs://bucket_name/??.txt: matches files with two characters followed by .txt in bucket_name
        /// * gs://bucket_name/[aeiou].txt: matches files that contain a single vowel character followed by .txt in bucket_name
        /// * gs://bucket_name/[a-m].txt: matches files that contain a, b, ... or m followed by .txt in bucket_name
        /// * gs://bucket_name/a/*/b: matches all files in bucket_name that match a/*/b pattern, such as a/c/b, a/d/b
        /// * gs://another_bucket/a.txt: matches gs://another_bucket/a.txt
        /// </summary>
        public InputList<string> FilePatterns
        {
            get => _filePatterns ?? (_filePatterns = new InputList<string>());
            set => _filePatterns = value;
        }

        [Input("sampleGcsFileSpecs")]
        private InputList<Inputs.EntryGcsFilesetSpecSampleGcsFileSpecGetArgs>? _sampleGcsFileSpecs;

        /// <summary>
        /// -
        /// Sample files contained in this fileset, not all files contained in this fileset are represented here.  Structure is documented below.
        /// </summary>
        public InputList<Inputs.EntryGcsFilesetSpecSampleGcsFileSpecGetArgs> SampleGcsFileSpecs
        {
            get => _sampleGcsFileSpecs ?? (_sampleGcsFileSpecs = new InputList<Inputs.EntryGcsFilesetSpecSampleGcsFileSpecGetArgs>());
            set => _sampleGcsFileSpecs = value;
        }

        public EntryGcsFilesetSpecGetArgs()
        {
        }
    }
}
